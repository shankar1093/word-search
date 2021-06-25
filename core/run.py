import argparse
import sys
from email_indexer import index_emails, search_word
from pprint import pprint

ERR_BUILD_TRIE_IGNORE = "`source_dir` not provided"


def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Command line to create trie")
    parser.add_argument(
        "--source_dir",
        type=str,
        help="Path to dir with emails",
        default=None,
    )

    parser.add_argument(
        "--trie",
        type=str,
        help="location of pickle representing the Trie",
        default=None,
    )
    parser.add_argument(
        "--target-directory",
        type=str,
        help="Location to move picle file.",
        default=None,
    )
    parser.add_argument(
        "--build_trie",
        action="store_true",
        help="Pass in path do dir with emails.",
        default=None,
    )

    parser.add_argument(
        "--search",
        action="store_true",
        help="Pass in path do trie.",
        default=None,
    )
    parser.add_argument("--word", type=str, help="word to search", default=None)

    parsed_args = parser.parse_args(args)

    if parsed_args.build_trie and not parsed_args.source_dir:
        raise ValueError(ERR_BUILD_TRIE_IGNORE)

    return parsed_args


def main(args=None):
    args = parse_args(args)

    if args.build_trie:
        index_emails(args.source_dir, args.target_directory)

    if args.search:
        word_path = search_word(args.word, args.trie)
        print(f"The word {args.word} appears in the following paths:")
        pprint(word_path)


main()