def mock_glob_single_file(*args, **kwargs):
    return ["test_file.txt"]

def mock_glob_no_file(*args, **kwargs):
    return []

def mock_glob_multiple_files(*args, **kwargs):
    return ["test1.txt", "test2.txt"]

def mock_open_file_content(*args, **kwargs):
    class MockFile:
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def read(self):
            return "Sample content"
    return MockFile(package.show.datetime)
