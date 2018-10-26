import requests

tableau_list_url = 'https://public.tableau.com/profile/api/{}/workbooks?count={}&index=0'
tableau_data_url = 'https://public.tableau.com/profile/api/workbook/AudinciasdeCustdia-Detalhamento'
base_share_url = 'https://public.tableau.com/views/' 


share_url = {}
share_url[1] = 'NovoSistemaCarcerrio/PAPorCadeia?:embed=y&:display_count=yes'
share_url[2] = 'MPM3_0-Segurana02-TaxaCrescimentoRoubosFurtoseOutrosDelitos/PAPrincipal?:embed=y&:display_count=yes&:toolbar=no'
share_url[3] = 'MPM3_0-Educao10-EsforoDocente/PAESF_DOC?:embed=y&:display_count=yes&publish=yes&:toolbar=no'


def tableau_data(profile, count):
    data = requests.get(tableau_list_url.format(profile, count)).json()

    for code, url in share_url.items():
        print('{}: {}'.format(code, url))

    for tableau in data:
        print(tableau)

    return [('teste', 'Teste'),
            ('mais_teste', 'Mais Teste')]
