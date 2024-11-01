## Signals
### O que é o Signals?
O signals nada mais é do que o padrão de projeto **Observer** aplicado no contexto de modelos dentro do Django. 

#### Como usar o Signals?
Dentro do módulo `models.py` podemos fazer uma função que seja responsável de dar uma ação para os *Observadores*:

```
def criar_profile(sender, instance, created, **kwargs):
	pass
```

Aqui temos que entender o que são os parâmetros que estamos usando dentro da nossa função:

* `sender` --- é o Objeto que está sendo observado
* `instance` --- se refere ao Objeto que será manipulado (Observador)
* `created` --- um boolean que vai ser verdadeiro apenas quando o Objeto está sendo criado


Levando em conta que sabemos como isso funciona, vamos fazer com que sempre que um usuário for criado, um *profile* seja criado para ele.

```
from django.contrib.auth.models import  User
from django.db.models.signals import  post_save

def  criar_profile(sender, instance, created, **kwargs):

	if  created:
		Profile.objects.create(usuario=instance)
	else:
		if  not  hasattr(instance, "profile"):
			Profile.objects.create(usuario=instance)

post_save.connect(receiver=cria_profile, sender=User)
``` 

Nossa função agora sempre irá criar um Profile para os Usuários que forem criados; E para os Usuários que por acaso não tem um Profile, quando forem alterados, eles também terão o Profile criado quando forem alterados.

#### Mas o que está fazendo com que a Função saiba que o Usuário foi criado?

Note que temos esta linha abaixo da função:

    post_save.connect(receiver=cria_profile, sender=User)

O signals observa eventos **antes** ou **após** alguma alteração no **Objeto** que está sendo observado. Ou seja, temos **post_save** para sinalizar que o evento será após o **sender** ser criado. 

### Organização correta do Signals
Agora que já abordamos sobre como usar o Signals, devemos ter em mente que não é uma boa prática mante-lo dentro do módulo de `models.py`.

Dentro da aplicação em que nosso `models.py` está, vamos criar um novo módulo com o nome `signals.py`. Dentro dele insira todo o código que criamos anteriormente. 

**Ainda não terminamos**, para que a função esteja funcionando, é preciso inserir o nosso módulo `criar_profile` seja reconhecido pelo modelo. 

Vamos em `app.py` e vamos adicionar o seguinte:

```
class ...(AppConfig):
	
	def  ready(self):
		import core.signals
```

Note que o método deve ficar dentro de  `class  CoreConfig(AppConfig)` (nome da classe no meu projeto).

Uma vez que você fez todos os passos, teste o que acabamos de fazer na seção do Admin para conferir se a criação de Usuário realmente vai criar um Profile. 

