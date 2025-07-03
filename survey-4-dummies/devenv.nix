{ pkgs, ... }:

{
  # Use Python 3.11 environment
  languages.python = {
    enable = true;
    version = "3.11";
    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };
  };

  # Install ollama as a system package if available, or provide a message
  packages = [
    pkgs.ollama
  ];

  enterShell = ''
    echo "Python virtual environment is ready."
    echo "Ollama must be running locally (see https://ollama.com/)."
  '';
}
