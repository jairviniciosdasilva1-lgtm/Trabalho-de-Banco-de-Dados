from conexao import supabase

def login(email, senha):
    res = supabase.table("usuario") \
        .select("*") \
        .eq("email", email) \
        .eq("senha", senha) \
        .execute()

    return res.data[0] if res.data else None

