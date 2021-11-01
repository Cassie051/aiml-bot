import unidecode
import aiml

def learn_aiml(kernel):
    kernel.learn("greetings_chat.aiml")
    kernel.learn("cuttings_chat.aiml")
    kernel.learn("color_chat.aiml")
    kernel.learn("style_chat.aiml")
    kernel.learn("sumup_chat.aiml")
    kernel.learn("farewell_chat.aiml")


def main():
    kernel = aiml.Kernel()
    learn_aiml(kernel)

    while True:
        input_text = input("> Człowiek: ")
        response = kernel.respond(unidecode.unidecode(input_text))
        print("Bot: " + response)

if __name__ == "__main__":
    main()