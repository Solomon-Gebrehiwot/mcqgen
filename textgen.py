import argparse
import os
import sys
from typing import Optional


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Minimal LangChain-based text generator supporting OpenAI and Ollama",
		formatter_class=argparse.ArgumentDefaultsHelpFormatter,
	)
	parser.add_argument(
		"--provider",
		choices=["openai", "ollama"],
		required=True,
		help="Model provider backend",
	)
	parser.add_argument(
		"--model",
		required=True,
		help="Model name to use (e.g., gpt-4o-mini, llama3.1:8b)",
	)
	parser.add_argument(
		"--prompt",
		"-p",
		required=True,
		help="Prompt text to generate from",
	)
	parser.add_argument(
		"--temperature",
		"-t",
		type=float,
		default=0.7,
		help="Sampling temperature",
	)
	parser.add_argument(
		"--max-tokens",
		"-m",
		type=int,
		default=None,
		help="Maximum tokens in the completion (if supported)",
	)
	parser.add_argument(
		"--dry-run",
		action="store_true",
		help="Print resolved configuration without calling the provider",
	)
	return parser.parse_args()


def run_generation(args: argparse.Namespace) -> int:
	if args.dry_run:
		print("Provider:\t" + args.provider)
		print("Model:\t\t" + args.model)
		print("Temperature:\t" + str(args.temperature))
		print("Max tokens:\t" + ("none" if args.max_tokens is None else str(args.max_tokens)))
		print("Prompt:\t\t" + args.prompt)
		return 0

	try:
		if args.provider == "openai":
			from langchain_openai import ChatOpenAI  # type: ignore

			api_key = os.environ.get("OPENAI_API_KEY")
			if not api_key:
				print("OPENAI_API_KEY is not set in the environment", file=sys.stderr)
				return 2

			llm = ChatOpenAI(
				model=args.model,
				temperature=args.temperature,
				max_tokens=args.max_tokens,
			)
		elif args.provider == "ollama":
			from langchain_ollama import ChatOllama  # type: ignore

			llm = ChatOllama(
				model=args.model,
				temperature=args.temperature,
			)
		else:
			print(f"Unsupported provider: {args.provider}", file=sys.stderr)
			return 2
	except ImportError as exc:
		print(
			f"Missing dependencies for provider '{args.provider}'. Install requirements first.\n{exc}",
			file=sys.stderr,
		)
		return 2

	try:
		response = llm.invoke(args.prompt)
	except Exception as exc:  # noqa: BLE001
		print(f"Generation failed: {exc}", file=sys.stderr)
		return 1

	content = getattr(response, "content", None)
	print(content if content is not None else str(response))
	return 0


def main() -> int:
	args = parse_args()
	return run_generation(args)


if __name__ == "__main__":
	sys.exit(main())

