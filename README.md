# Embedding Pictures

This exercise contains five small programs which illustrate embedding topics
in Ocean and on the D-Wave QPUs, for Training features.

## Exercise 1

At the command line, to run the demo:

```bash
python clique_embedding_chimera.py 8
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

The program will produce a picture with a left and right side. The left side
is an 8-clique and the right picture is an example Chimera embedding of an
8-clique.

## Exercise 2

At the command line, to run the demo:

```bash
python clique_embedding_pegasus.py 8
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

The program will produce a picture with a left and right side. The left side
is an 8-clique and the right picture is an example Pegasus embedding of an
8-clique.

## Exercise 3

At the command line, to run the demo:

```bash
python clique_break_list_broken.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

The output will have four sections:

* The embedding of the 4-clique on Chimera
* The solutions to the 4-clique graph partitioning problem
* The solutions, expressed in terms of whether or not the individual logical variables represent broken chains or not. (A ``True`` indicates a broken chain)
* The indices of the broken chains

This exercise shows the specific chains which have broken. It's useful
to see how chains break at small values of ``chainstrength``.

## Exercise 4

At the command line, to run the demo:

```bash
python explore_embed_clique_chimera.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

The output of the program will be a typical Chimera embedding of a 4-clique.

## Exercise 5

At the command line, to run the demo:

```bash
python explore_embed_clique_pegasus.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

The output of the program will be a typical Pegasus embedding of a 4-clique.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
