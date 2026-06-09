import boto3
import json

def call_bedrock(prompt):
    client = boto3.client(
        "bedrock-runtime",
        region_name="us-east-1"
    )

    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ]
    })

    response = client.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    return result["output"]["message"]["content"][0]["text"]

if __name__ == "__main__":
    print("🤖 Amazon Bedrock AI — Ask me anything!")
    print("💡 Type your question and press Enter")
    print("❌ Type 'exit' to quit\n")
    print("-" * 50)

    while True:
        question = input("\n👤 You: ")

        if question.lower() == "exit":
            print("\n👋 Goodbye! See you at AWS Community Day!")
            break

        if question.strip() == "":
            print("Please type a question!")
            continue

        print("\n🤖 AI is thinking...")
        answer = call_bedrock(question)
        print(f"\n💬 AI: {answer}")
        print("-" * 50)
