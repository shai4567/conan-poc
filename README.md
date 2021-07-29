# Introduction to Conan package manager

## Prerequisites

* Conan installed
    * Or simply run:
    ```bash
    task conan
    ```
    * run conan -v - in order to make sure it is working
* cmake installed (Our current hands-on example using cmake sample app)
* Change on phase2/conanfile.py - line 24 --> Your path to the project

## Usage:
Each phase presenting another ability of Conan:
* Phase1: presenting Conan as package manager tool
    * Packaging the compiled code + dependencies 
    * Uploading to Artifactory registry
    * Collection the data as consumer
    * Using the dependecies provided by Conan (From the producer)

* Phase2: presenting conan as bulding tool as well
    * conanfile.py Has now build step
    * the build step using cmake class in order to trigger cmake build command as a part of the conan operation

* Phase3: presenting conan as abilities to gather source data from SCM
    * Source method has been added to conanfile.py
    * Conan will now clone the project we need to compile + run cmake operation + pack the chosen outputs , and everything is a part of a single packaging operation

## Some Conan base commands:
\* Please note:
Most of the commands can be referenced to specific remote using -r {{REMOTE_NAME}}

* Searching for packages:
```bash
conan search {{NAME}}
```
\* If you will not specify searching argument it will return all existing packages

* Get list of Conan remotes:
```bash
conan remote list
```
* Remove Conan package:
```bash
conan remove {{PACKAGENAME}}/{{PACKAGE_VERSION}}@{{USER}}/{{CHANNEL}}
```
## Useful commands:

* Creating Conan package:
```bash
conan create {{PATH_TO_CONANFILE}} {{USER}}/{{CHANNEL}}
```
Example used in the p.o.c: conan create . mobileye/testing

* Adding Conan remote:
```bash
conan remote add {{REMOTE_NAME}} {{REMOTE_PATH}}
```
Example used in the p.o.c:
```bash
conan remote add mobileye https://artifactory.sddc.mobileye.com:443/artifactory/api/conan/di-dev-conan-local
```

* Assign User to remote:
```bash
conan user {{USER_NAME}} -p {{PASSWORD}} -r {{REMOTE_NAME}}
```
DISCLAIMER: Make sure the user got credentials to make changes in the remote conan repo

* Uploading Conan package to a remote:
```bash
conan upload {{PACKAGENAME}}/{{PACKAGE_VERSION}}@{{USER}}/{{CHANNEL}} -r {{REMOTE_NAME}} --all
```
Example used in the p.o.c: conan upload Hello/0.0.2@moileye/testing -r mobileye --all

* Installing Conan package from a remote:
```bash
conan install {{PATH_TO_CONANFILE_TXT}} -r {{REMOTE_NAME}}
```
Example used in the p.o.c: conan install . -r mobileye
