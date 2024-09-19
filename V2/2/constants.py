from pathlib import Path

# Définir le chemin du répertoire courant
CUR_DIR = Path(__file__).resolve().parent

# Définir le chemin du répertoire "data"
DATA_DIR = CUR_DIR / "data"

if __name__ == "__main__":
    print(DATA_DIR)
    print("-" * 50)
    print(CUR_DIR)