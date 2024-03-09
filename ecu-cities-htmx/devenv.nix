{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "hello";

  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.version = "3.12.0";
  languages.python.venv = {
	  enable = true;
	  requirements = ./requirements.txt;
  };
}
