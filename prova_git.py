# prova_git.py

import os

def main():
    arquivo_respostas = "respostas_git.txt"
    if os.path.exists(arquivo_respostas):
        print("⚠️ A prova já foi realizada. Você não pode refazê-la.\n*** Agora envie suas respostas! ***")
        return

    print("🛠️ Bem-vindo à Prova de Git!")
    nome = input("Digite seu nome completo: ").strip()
    print("\nResponda às questões abaixo. Digite apenas a letra (a, b, c, d ou e).\n")

    perguntas = [
        {
            "pergunta": "\n1. O que faz o comando 'git init'?",
            "alternativas": [
                "a) Baixa um repositório remoto",
                "b) Envia arquivos para o GitHub",
                "c) Inicia um novo repositório Git local",
                "d) Mostra os arquivos modificados",
                "e) Cria um novo branch"
            ],
            "correta": "c"
        },
        {
            "pergunta": "\n2. Para que serve o 'git clone'?",
            "alternativas": [
                "a) Para criar commits",
                "b) Para iniciar um repositório",
                "c) Para deletar um branch",
                "d) Para copiar um repositório remoto",
                "e) Para atualizar o repositório local"
            ],
            "correta": "d"
        },
        {
            "pergunta": "\n3. Qual comando mostra o estado atual dos arquivos?",
            "alternativas": [
                "a) git log",
                "b) git status",
                "c) git commit",
                "d) git diff",
                "e) git push"
            ],
            "correta": "b"
        },
        {
            "pergunta": "\n4. Como adicionamos arquivos à staging area?",
            "alternativas": [
                "a) git add",
                "b) git push",
                "c) git commit",
                "d) git init",
                "e) git branch"
            ],
            "correta": "a"
        },
        {
            "pergunta": "\n5. Qual o comando para salvar as alterações com uma mensagem?",
            "alternativas": [
                "a) git save",
                "b) git commit -m 'mensagem'",
                "c) git stage",
                "d) git message",
                "e) git log -m"
            ],
            "correta": "b"
        },
        {
            "pergunta": "\n6. Como visualizar o histórico de commits?",
            "alternativas": [
                "a) git commit",
                "b) git status",
                "c) git history",
                "d) git log",
                "e) git track"
            ],
            "correta": "d"
        },
        {
            "pergunta": "\n7. O que faz o comando 'git push'?",
            "alternativas": [
                "a) Traz alterações do repositório remoto",
                "b) Salva os arquivos localmente",
                "c) Envia alterações locais para o repositório remoto",
                "d) Mostra os commits",
                "e) Adiciona arquivos à staging area"
            ],
            "correta": "c"
        },
        {
            "pergunta": "\n8. E o comando 'git pull'?",
            "alternativas": [
                "a) Puxa alterações do remoto para local",
                "b) Salva alterações",
                "c) Cria novo commit",
                "d) Altera o branch principal",
                "e) Remove arquivos do staging"
            ],
            "correta": "a"
        },
        {
            "pergunta": "\n9. Como criamos um novo branch?",
            "alternativas": [
                "a) git new branch",
                "b) git branch create",
                "c) git checkout -b nome",
                "d) git init branch",
                "e) git start branch"
            ],
            "correta": "c"
        },
        {
            "pergunta": "\n10. Qual comando usamos para mudar de branch?",
            "alternativas": [
                "a) git change",
                "b) git move",
                "c) git swap",
                "d) git checkout nome-do-branch",
                "e) git jump"
            ],
            "correta": "d"
        }
    ]

    respostas = []
    acertos = 0

    for item in perguntas:
        print(item["pergunta"])
        for alternativa in item["alternativas"]:
            print(alternativa)
        resposta = input("Sua resposta: ").strip().lower()

        while resposta not in ['a', 'b', 'c', 'd', 'e']:
            resposta = input("❗ Digite uma alternativa válida (a, b, c, d ou e): ").strip().lower()

        correta = item["correta"]
        if resposta == correta:
            acertos += 1

        respostas.append(f"{item['pergunta']}\nResposta: {resposta.upper()} | Correta: {correta.upper()}\n")

    nota = (acertos / len(perguntas)) * 10

    with open(arquivo_respostas, "w", encoding="utf-8") as f:
        f.write(f"Aluno: {nome}\nNota: {nota:.1f}/10\n\n")
        f.write("\n".join(respostas))

    print(f"\n✅ Prova finalizada! Sua nota: {nota:.1f}/10")
    print(f"As respostas foram salvas no arquivo '{arquivo_respostas}'.")

if __name__ == "__main__":
    main()
