{ pkgs, lib, config, inputs, ... }:

{
  packages = [ pkgs.ollama ];

  languages.python.enable = true;
  languages.python.package = pkgs.python312;
  languages.python.venv.enable = true;
  languages.python.venv.requirements = "./requirements.txt";
}
