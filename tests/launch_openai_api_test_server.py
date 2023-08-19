"""
Launch an OpenAI API server with multiple model workers.
"""
import os


def launch_process(cmd):
    os.popen(cmd)


if __name__ == "__main__":
    launch_process("python3 -m fastchat.serve.controller")
    launch_process("python3 -m fastchat.serve.openai_api_server --host 0.0.0.0")

    models = [
        # "lmsys/vicuna-7b-v1.3",
        # "lmsys/fastchat-t5-3b-v1.0",
        # "../../chatglm2-6b",
        # "mosaicml/mpt-7b-chat",
        # "../../Qwen-7B-Chat",
        "../../Qwen-7B-Chat",
    ]

    for i, model_path in enumerate(models):
        launch_process(
            f"CUDA_VISIBLE_DEVICES={i} python3 -m fastchat.serve.model_worker "
            f"--model-path {model_path} --load_8bit True --port {30000+i} --model-names 'gpt-3.5-turbo' --limit-worker-concurrency 5 --worker http://localhost:{30000+i}"
        )

    while True:
        pass
