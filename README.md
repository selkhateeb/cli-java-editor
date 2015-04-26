
Introduction
------------
Command line utility to edit java projects.

Installation
------------
`python setup.py install`

This will install `je` in your python bin path. Make sure it is exported as
part of `PATH`.

Usage
-----
### Assumptions
- All projects must be in a `git` SCM. Used to find the base directory.
- `git` must be installed.


### `find` classes
This works similar to Eclipse's way of finding classes.

```shell
# cd java_git_project

# find java files by class name camelcase pattern
$ je find VerC
<root_path>/gerrit/gerrit-server/src/main/java/com/google/gerrit/server/schema/SchemaVersionCheck.java
<root_path>/gerrit/gerrit-solr/src/main/java/com/google/gerrit/solr/IndexVersionCheck.java
<root_path>/gerrit/gerrit-sshd/src/main/java/com/google/gerrit/sshd/commands/VersionCommand.java

# Use --package to get the fully quilfied name
$ je find VerC --package
com.google.gerrit.server.schema.SchemaVersionCheck
com.google.gerrit.solr.IndexVersionCheck
com.google.gerrit.sshd.commands.VersionCommand

```