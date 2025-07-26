{ pkgs, ... }:

{
  # Use the overridden Python
  languages.python = {
    enable = true;
    # Tell devenv to use our custom Python
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
