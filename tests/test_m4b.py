import factory

from ffhilfe.m4b.metadata import Chapter, Metadata, Stream


def timeline():
    time = 0
    while True:
        yield time
        time += 1


timeline = timeline()


class ChapterFactory(factory.Factory):

    class Meta:
        model = Chapter

    title = factory.Sequence(lambda n: f'Chapter {n}')
    start = factory.Iterator(timeline)
    end = factory.Iterator(timeline)
    timebase = (1, 1000)

    @classmethod
    def _setup_next_sequence(cls):
        return 1


class StreamFactory(factory.Factory):

    class Meta:
        model = Stream

    title = factory.Faker('sentence', nb_words=4)


class MetadataFactory(factory.Factory):

    class Meta:
        model = Metadata

    title = factory.Faker('sentence', nb_words=4)
    artist = factory.Faker('name')
    chapters = factory.List([
        factory.SubFactory(ChapterFactory) for _ in range(5)
    ])
    stream = factory.SubFactory(StreamFactory, title=factory.SelfAttribute('..title'))


def test_chapter_factory():
    ChapterFactory.reset_sequence()
    chapter_1 = ChapterFactory()
    chapter_2 = ChapterFactory()
    chapter_3 = ChapterFactory()

    assert chapter_1.title == 'Chapter 1'
    assert chapter_2.title == 'Chapter 2'
    assert chapter_3.title == 'Chapter 3'

    assert chapter_1.start < chapter_1.end
    assert chapter_1.end < chapter_2.start
    assert chapter_2.start < chapter_2.end
    assert chapter_2.end < chapter_3.start
    assert chapter_3.start < chapter_3.end


def test_stream_factory():
    stream = StreamFactory()

    assert type(stream.title) == str


def test_metadata_factory():
    metadata = MetadataFactory()

    assert len(metadata.chapters) == 5
    for chapter in metadata.chapters:
        assert type(chapter) == Chapter
        assert type(chapter.title) == str
        assert chapter.start < chapter.end
    assert metadata.title == metadata.stream.title


def test_create_metadata():
    metadata = Metadata(
        title='The title',
        artist='The artist',
        chapters=(
            Chapter('1', 0, 399),
            Chapter('2', 400, 499),
            Chapter('3', 500, 699),
        ),
        stream=Stream('The title')
    )

    assert metadata.title == 'The title'
