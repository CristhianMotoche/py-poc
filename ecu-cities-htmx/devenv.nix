{ pkgs, ... }:

let
  pwd = builtins.getEnv "PWD";
in
{
  # https://devenv.sh/basics/
  env.TEMPLATE_DIR = "${pwd}/templates";

  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.version = "3.12.0";
  languages.python.venv = {
    enable = true;
    requirements = ./requirements.txt;
  };

  # scripts
  scripts.run.exec = ''
    python dist
  '';
  scripts.compile-watch.exec = ''
    coconut . dist -w
  '';
}
