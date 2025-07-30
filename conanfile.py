from conan import ConanFile
from conan.tools.files import copy

class TestUtilsConan(ConanFile):
    name = "test_utils"
    version = "1.0"
    license = "MIT"
    scm = {
        "type": "git",
        "url": "https://github.com/nick-a-schneider/test_utils.git",
        "revision": "auto"  # automatically uses current commit hash
    }
    package_type = "header-library"
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        copy(self, "*.h", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
