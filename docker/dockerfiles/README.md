# Dockerfile Commands

| Command | Descirption |
| :------ | ----------- |
| From | This is the first command in the Dockerfile. Without this, we
can’t build an image. We can build the image just with this command.
when we build just with FROM, we are actually taking the base image CMD
whenever the image is instantiated. |
| CMD | This command is used to give the default commands when the image
is instantiated, it doesn't execute while build stage. There should be
only one CMD per Dockerfile, you can list multiple but the last one will
be executed. |
| ENTRYPOINT | ENTRYPOINT is used as an executable for the container.
ex: Default ENTRYPOINT for ubuntu is ```bash``` |
| WORKDIR | WORKDIR sets the working directory for all the consecutive
commands. we can have multiple WORKDIR commands and will be appended
with a relative path. |
| ENV | ENV sets the environment variables for the subsequent
instructions in the build stage. |
| COPY | COPY is used to copy files or directories from source host
filesystem to a destination in the container file system. |
| LABEL | LABEL is used to add some metadata to the image. if we use the
same label as the base image and the most recent label value is
applied.|
| RUN | RUN executes the instructions in a new layer on top of the
existing image and commit those layers and the resulted layer will be
used for the next instructions in the Dockerfile. |
| ADD | ADD is used to add files or directories and remote files from
URL from source host filesystem to a destination in the container file
system. |
| .dockerignore | Whenever we build the image at the root level, the
entire context is sent to the Docker daemon. Sometimes we don’t need to
send all the content to Docker daemon, those files or directories should
be added to this .dockerignore file. |
| ARG | ARG is used to pass some arguments to consecutive instructions
and this is only command other than a comment can be used before FROM. |
| EXPOSE | EXPOSE is used as documentation for the port. This is just a
communication between the person who builds the image and the person who
runs the container. It doesn’t serve any other purpose other than
documentation. |
| USER | USER instruction sets the user name and optionally the user
group to use when running the image and for any instructions that follow
it in the Dockerfile |
| VOLUME | VOLUME is used to create a mount point with the specified
name. Following are the examples of Dockerfile and running
instructions. |

## ADD vs COPY [Link](https://phoenixnap.com/kb/docker-add-vs-copy)

Although ```ADD``` and ```COPY``` are slight differences in the scope of their function, they essentially perform the same task

### ADD

* Copy files/directories to a file system of the specified container.
* If the source is a directory, ADD copies everything inside of it (including file system metadata).
* ADD can also copy files from a URL
* It copies compressed files, automatically extracting the content in the given destination. 

### COPY

COPY only has only one assigned function. Its role is to duplicate files/directories in a specified location in their existing format. This means that it doesn't deal with extracting a compressed file, but rather copies it as-is.

## Which to use?

Docker's official documentation notes that COPY should always be the go-to instruction as it is more transparent than ADD.

*Note:* To build an image run the following command:
```bash
docker build -t ImageName:TagName dir
```
* ```-t``` -- is to mention a tag to the image
* ImageName -- This is the name you want to give to your image
* TagName -- This is the tag you want to give to your image
* Dir -- The directory where the Docker File is present
