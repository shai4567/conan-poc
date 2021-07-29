from conans import ConanFile, CMake, tools

class HelloConan(ConanFile):
    name = "Hello"
    version = "0.0.2"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def package(self):
        self.copy("*.h", dst="include", src="/homes/shaiha/conan_poc/phase1/hello")
        self.copy("*.a", dst="lib", src="/homes/shaiha/conan_poc/phase1/hello/lib", keep_path=False)
        self.copy("*greet*", dst="bin", src="/homes/shaiha/conan_poc/phase1/hello/bin", keep_path=False)
