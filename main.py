import argparse
import asyncio

from modules.reader import read_from_file
from modules.analyzer import word_count, word_frequency, find_matches, translate_text
from modules.utils import simulated_long_running_task


def main():

    # Para simular uma tarefa assíncrona
    loop = asyncio.get_event_loop()
    loop.run_until_complete(simulated_long_running_task())
    
    parser = argparse.ArgumentParser(description="Sistema de Análise e Processamento de Textos")
    parser.add_argument("filename", help="O nome do arquivo a ser processado")
    parser.add_argument("--count", action="store_true", help="Retorna o total de palavras no arquivo")
    parser.add_argument("--freq", action="store_true", help="Retorna a frequência de cada palavra no arquivo")
    parser.add_argument("--pattern", help="Padrão regex para encontrar correspondências no texto")
    parser.add_argument("-tr", "--translate", help="Tradução do texto para um idioma específico. Use o formato 'source:target'. Se o 'source' for omitido, será utilizado o modo de auto-detecção.", default=None)

    args = parser.parse_args()
    text = read_from_file(args.filename)

    if args.count:
        print(f"Total de palavras: {word_count(text)}")
    
    if args.freq:
        freq = word_frequency(text)
        for word, count in freq.items():
            print(f"{word}: {count}")
    
    if args.pattern:
        matches = find_matches(text, args.pattern)
        for match in matches:
            print(f"Correspondência encontrada: {match}")
    
    if args.translate:
        source_language, target_language = (args.translate.split(":") + ["auto", "pt"])[:2]
        translated_text = translate_text(text, to_language=target_language, from_language=source_language)
        print(f"Translated Text: {translated_text}")
    

if __name__ == "__main__":
    main()
