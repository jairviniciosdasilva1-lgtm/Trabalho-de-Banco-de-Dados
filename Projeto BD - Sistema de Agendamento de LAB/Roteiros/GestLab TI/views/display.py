def linha():
    print("-" * 60)


def titulo(texto):
    linha()
    print(f"  {texto}")
    linha()


def tabela(dados, campos, cabecalhos=None):
    if not dados:
        print("  Nenhum registro encontrado.")
        return

    cabecalhos = cabecalhos or campos

    larguras = []
    for i, campo in enumerate(campos):
        max_val = max(len(str(d.get(campo, "") or "")) for d in dados)
        larguras.append(max(max_val, len(cabecalhos[i])))

    cabecalho = "  " + "  ".join(str(cabecalhos[i]).ljust(larguras[i]) for i in range(len(campos)))
    print(cabecalho)
    print("  " + "  ".join("-" * l for l in larguras))

    for d in dados:
        linha_str = "  " + "  ".join(str(d.get(campo, "") or "").ljust(larguras[i]) for i, campo in enumerate(campos))
        print(linha_str)


def sucesso(msg):
    print(f"\n  ✓ {msg}\n")


def erro(msg):
    print(f"\n  ✗ Erro: {msg}\n")


def pausar():
    input("\n  Pressione Enter para continuar...")
