from django.db import models


class APIConfigLoja:
    """
    API para facilitar o acesso a configloja de configuracao do banco de dados
    """
    def __init__(self):
        conf = Configloja.objects.get(cd_chave='ZIM   1')
        self.cd_regiao, self.sg_loja = conf.no_conf.split(':')[:2]
        self.cd_regiao = int(self.cd_regiao)


class APIConsultaCliente:
    """
    API para utilizar as imagens da aplicação 'CONSULTA'
    """
    def __init__(self):
        if not isinstance(self, Cliente):
            raise Exception('aceita somente objetos de Cliente')
        self.conf = APIConfigLoja()

    def get_imagens(self):
        """
        Retorna lista de imagens do cliente
        """
        return 'https://{}.claudinosa.com.br/{}/index/{}'.format(
            'theconsulta' if self.conf.sg_loja == 'THE' else self.conf.sg_loja.lower(),
            'api' if self.conf.sg_loja == 'THE' else 'consulta/api',
            str(self.cd_cliente))
    
    def get_imagem_url(self, codigo):
        """
        Retorna URL com a imagem do cliente
        """
        return 'https://{}.claudinosa.com.br/{}/get_image/{}'.format(
            'theconsulta' if self.conf.sg_loja == 'THE' else self.conf.sg_loja.lower(),
            'api' if self.conf.sg_loja == 'THE' else 'consulta/api',
            str(codigo))
    
    def get_foto(self):
        """
        Retornar a foto do cliente
        """
        import requests
        id = None
        response = requests.get(self.get_imagens())
        data = response.json()
        for row in data:
            if row['FlFoto'] == '1':
                id = row['Id']
                break

        if id is not None:
            return self.get_imagem_url(id)
            


class Cliente(models.Model, APIConsultaCliente):
    cd_regiao = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Região')
    cd_cliente = models.DecimalField(max_digits=8, decimal_places=0)
    no_apelido = models.CharField(max_length=20)
    no_cliente = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_est_civil = models.CharField(max_length=1, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    no_profissao = models.CharField(max_length=20, blank=True, null=True)
    no_cid_natural = models.CharField(max_length=20, blank=True, null=True)
    cd_uf_natural = models.CharField(max_length=2, blank=True, null=True)
    no_funcao = models.CharField(max_length=15, blank=True, null=True)
    no_endereco = models.CharField(max_length=45, blank=True, null=True)
    no_bairro = models.CharField(max_length=20, blank=True, null=True)
    no_cidade = models.CharField(max_length=35, blank=True, null=True)
    uf_residencia = models.CharField(max_length=2, blank=True, null=True)
    no_ponto_refer = models.CharField(max_length=50, blank=True, null=True)
    ao_resid_tipo = models.CharField(max_length=1, blank=True, null=True)
    ao_resid_tempo = models.CharField(max_length=10, blank=True, null=True)
    vl_aluguel = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vl_salario = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cd_loja_origem = models.CharField(max_length=3, blank=True, null=True)
    cd_representante = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    dt_admissao = models.DateField(blank=True, null=True)
    nr_cep_residencia = models.CharField(max_length=10, blank=True, null=True)
    tt_azul = models.SmallIntegerField(blank=True, null=True)
    tt_verde = models.SmallIntegerField(blank=True, null=True)
    tt_vermelho = models.SmallIntegerField(blank=True, null=True)
    tp_cliente = models.CharField(max_length=2, blank=True, null=True)
    nr_fone_amigo = models.CharField(max_length=12, blank=True, null=True)
    no_firma = models.CharField(max_length=45, blank=True, null=True)
    no_endereco_fir = models.CharField(max_length=45, blank=True, null=True)
    no_bairro_fir = models.CharField(max_length=20, blank=True, null=True)
    no_cidade_fir = models.CharField(max_length=20, blank=True, null=True)
    uf_fir = models.CharField(max_length=2, blank=True, null=True)
    nr_fone_fir = models.CharField(max_length=12, blank=True, null=True)
    no_pai = models.CharField(max_length=40, blank=True, null=True)
    no_mae = models.CharField(max_length=40, blank=True, null=True)
    nr_fone_cliente = models.CharField(max_length=12, blank=True, null=True)
    dt_cadastramento = models.DateField(blank=True, null=True)
    fl_situacao = models.CharField(max_length=1, blank=True, null=True)
    ao_sit_atu_cen = models.CharField(max_length=1, blank=True, null=True)
    cd_area_entrega = models.CharField(max_length=4, blank=True, null=True)
    cd_area_cobranca = models.CharField(max_length=4, blank=True, null=True)
    cd_empresa_fun = models.CharField(max_length=2, blank=True, null=True)
    sg_filial_fun = models.CharField(max_length=3, blank=True, null=True)
    fl_mala_direta = models.CharField(max_length=1, blank=True, null=True)
    fl_alterado = models.CharField(max_length=1, blank=True, null=True)
    qt_tempo_serv = models.SmallIntegerField(blank=True, null=True)
    nr_identidade = models.CharField(max_length=12, blank=True, null=True)
    sg_loja = models.CharField(max_length=3, blank=True, null=True)
    fl_conceito = models.CharField(max_length=3, blank=True, null=True)
    cp_cp = models.CharField(max_length=3, blank=True, null=True)
    cd_matricula = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    dt_cep = models.DateField(blank=True, null=True)
    cd_cidade = models.CharField(max_length=6, blank=True, null=True)
    nr_ramal = models.CharField(max_length=4, blank=True, null=True)
    cd_pesquisa = models.CharField(max_length=3, blank=True, null=True)
    cd_vendedor = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    fl_clipar = models.CharField(max_length=1, blank=True, null=True)
    no_emissor = models.CharField(max_length=10, blank=True, null=True)
    cd_uf_ident = models.CharField(max_length=2, blank=True, null=True)
    cd_bairro = models.CharField(max_length=6, blank=True, null=True)
    cd_bairro_fir = models.CharField(max_length=6, blank=True, null=True)
    cd_cid_natural = models.CharField(max_length=6, blank=True, null=True)
    cd_cidade_fir = models.CharField(max_length=6, blank=True, null=True)
    no_logradouro = models.CharField(max_length=30, blank=True, null=True)
    cd_rua = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    cd_avalista = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    cd_setor = models.CharField(max_length=4, blank=True, null=True)
    cd_lote = models.CharField(max_length=4, blank=True, null=True)
    no_compend = models.CharField(max_length=90, blank=True, null=True)
    tt_canc = models.SmallIntegerField(blank=True, null=True)
    tt_exc = models.SmallIntegerField(blank=True, null=True)
    tt_av = models.SmallIntegerField(blank=True, null=True)
    fl_conceito1 = models.CharField(max_length=3, blank=True, null=True)
    cd_chave = models.CharField(primary_key=True, max_length=10, editable=False)
    cd_nomcod = models.CharField(max_length=53, blank=True, null=True)
    no_chvend = models.CharField(max_length=127, blank=True, null=True)
    no_endvirnr = models.CharField(max_length=9, blank=True, null=True)
    no_endvirbl = models.CharField(max_length=7, blank=True, null=True)
    no_endvirap = models.CharField(max_length=9, blank=True, null=True)
    no_endvir = models.CharField(max_length=88, blank=True, null=True)
    no_endvirst = models.CharField(max_length=8, blank=True, null=True)
    no_endvirlt = models.CharField(max_length=8, blank=True, null=True)
    no_endvir1 = models.CharField(max_length=90, blank=True, null=True)
    id_origin = models.CharField(max_length=3, blank=True, null=True)
    id_remote = models.CharField(max_length=3, blank=True, null=True)
    dth_criacao = models.DateTimeField()
    dth_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return '{} - {}'.format(self.cd_chave, self.no_cliente)
    
    @property
    def tem_documento(self):
        return bool(self.documento_set.all())
    
    @property
    def tem_telefone(self):
        return bool(self.clientefone_set.all())

    def get_foto_default(self):
        return 'img/user.png'
    
class Documento(models.Model):
    cd_regiao = models.DecimalField(max_digits=2, decimal_places=0)
    cd_cliente = models.DecimalField(max_digits=8, decimal_places=0)
    cd_indicador = models.CharField(max_length=2)
    tp_documento = models.CharField(max_length=2)
    nr_documento = models.CharField(max_length=25, blank=True, null=True)
    cd_chave = models.CharField(primary_key=True, max_length=12)
    #cd_chave_cli = models.CharField(max_length=10, blank=True, null=True)
    cd_chave_cli = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL, db_column='cd_chave_cli')
    cd_chave_tpnr = models.CharField(max_length=27, blank=True, null=True)
    id_origin = models.CharField(max_length=3, blank=True, null=True)
    id_remote = models.CharField(max_length=3, blank=True, null=True)
    dth_criacao = models.DateTimeField()
    dth_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documento'


class ClienteFone(models.Model):
    cd_regiao = models.DecimalField(max_digits=2, decimal_places=0)
    cd_cliente = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    tp_fone = models.CharField(max_length=2, blank=True, null=True)
    nr_telefone = models.CharField(max_length=13, blank=True, null=True)
    cd_chave = models.CharField(primary_key=True, max_length=12)
    cd_chave_cli = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL, db_column='cd_chave_cli')
    id_origin = models.CharField(max_length=3, blank=True, null=True)
    id_remote = models.CharField(max_length=3, blank=True, null=True)
    dth_criacao = models.DateTimeField()
    dth_atualizacao = models.DateTimeField()
    fl_msg = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente_fone'


class Tablinha(models.Model):
    cd_linha = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    no_linha = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablinha'

    def __str__(self):
        return self.no_linha


class Configloja(models.Model):
    sg_loja = models.CharField(max_length=3)
    cd_conf = models.CharField(max_length=4, blank=True, null=True)
    no_conf = models.CharField(max_length=35, blank=True, null=True)
    fl_conf = models.CharField(max_length=1, blank=True, null=True)
    nr_confa = models.CharField(max_length=91, blank=True, null=True)
    nr_confn = models.IntegerField(blank=True, null=True)
    dt_inclusao = models.DateField(blank=True, null=True)
    dt_encerra = models.DateField(blank=True, null=True)
    dt_inativo = models.DateField(blank=True, null=True)
    dt_inicio = models.DateField()
    cd_chave = models.CharField(primary_key=True, max_length=7)

    class Meta:
        managed = False
        db_table = 'configloja'