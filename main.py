from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client
import google.ads.googleads.client as ads_client

app = FastAPI()

# Configurações (Use as mesmas que já testamos)
SUPABASE_URL = "https://gyoqpcxemjxmejatcnol.supabase.co"
SUPABASE_KEY = "sb_secret_MC-ksJc-h9EO4tFWlZWUEQ_7hzsrk3Z"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class OtimizacaoRequest(BaseModel):
    campanha_id: str
    customer_id: str
    novos_titulos: list

@app.post("/otimizar")
async def aplicar_otimizacao(data: OtimizacaoRequest):
    try:
        # 1. Conecta ao Google Ads
        client = ads_client.GoogleAdsClient.load_from_storage("google-ads.yaml")
        
        # 2. Lógica para atualizar o anúncio (Simplificada)
        print(f"Aplicando {data.novos_titulos} na campanha {data.campanha_id}")
        
        # 3. Atualiza o status no Supabase para o Frontend saber que mudou
        supabase.table("logs_ia_sugestoes").update({"status_execucao": "aplicado"}).eq("id_campanha", data.campanha_id).execute()
        
        return {"status": "sucesso"}
    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}
