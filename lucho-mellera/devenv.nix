{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo hello from $GREET";

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.version = "3.12.0";
  languages.python.venv = {
    enable = true;
    requirements = ./requirements.txt;
  };
}
