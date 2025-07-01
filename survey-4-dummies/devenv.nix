# devenv.nix
# See https://devenv.sh/reference/options/ for more options
{
  inputs = {
    python = "3.11";
    ollama = "latest";
  };

  shell = [
    "pip install -r requirements.txt"
    "echo 'Ollama must be running locally.'"
  ];

  # Add more configuration as needed
}
