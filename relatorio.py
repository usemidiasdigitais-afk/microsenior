import os
from supabase import create_client
import requests

# Configurações do Banco
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

def gerar_resumo_semanal():
    # 1. Busca as otimizações dos últimos 7 dias no Supabase
    res = supabase.table("logs_otimizacao").select("*").execute()
    logs = res.data
    
    total = len(logs)
    texto_relatorio = f"📊 *Relatório Semanal Microsenior Ads*\n\nEsta semana, nossa IA realizou *{total}* otimizações nas suas campanhas.\n"
    
    for log in logs[:5]: # Mostra as 5 principais
        texto_relatorio += f"\n✅ Campanha: {log['campanha_nome']}\n   Ação: {log['acao']}"

    # 2. Enviar via Webhook (Pode ser para o seu WhatsApp via Zapier/Make ou E-mail)
    # Aqui usaremos um exemplo de Webhook simples
    webhook_url = "SUA_URL_DO_ZAPIER_OU_MAKE_AQUI"
    requests.post(webhook_url, json={"mensagem": texto_relatorio})
    
    print("Relatório enviado com sucesso!")

if __name__ == "__main__":
    gerar_resumo_semanal()
