from models import Cidade
from django.core.cache import cache

def cidades(request):
    # Get from cache if it already is there
    cidades_disponiveis = cache.get('CIDADES_DISPONIVEIS', None)
    if not cidades_disponiveis:
        cidades_disponiveis = Cidade.objects.filter(ativo=True).values('slug', 'nome')
        cache.set('CIDADES_DISPONIVEIS', list(cidades_disponiveis))

    return {
            'CIDADES_DISPONIVEIS': cidades_disponiveis,
        }

