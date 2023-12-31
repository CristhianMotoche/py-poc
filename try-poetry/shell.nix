{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [
      pkgs.python37
      pkgs.python37Packages.poetry
    ];

    shellHook =
      ''
      export SHELL=$(which zsh)
      zsh
      '';
  }
