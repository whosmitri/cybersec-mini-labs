# Relatório de Investigação | Análise de Autenticações SSH

* **Ambiente:** Laboratório de Segurança da Informação
* **Arquivo analisado:** `auth.log`
* **Data dos registros:** 08 de novembro
* **Tipo de análise:** Investigação de autenticações SSH

## 1. Resumo do incidente

Durante a análise do arquivo auth.log, foram identificadas quatro tentativas malsucedidas de autenticação SSH, todas originadas do endereço IP `192.0.2.45`.

Posteriormente, foi registrada uma autenticação bem-sucedida para o usuário analyst, utilizando o mesmo endereço IP.

Após o acesso, foi aberta uma sessão SSH e identificado o uso do comando `/usr/bin/id` por meio do sudo.

Alguns minutos depois, foi registrada outra autenticação bem-sucedida, desta vez para a conta backup, utilizando chave pública SSH e com origem no endereço IP `192.0.2.80`.

Os acontecimentos apresentam possíveis indicadores de atividade suspeita, mas não são suficientes, isoladamente, para confirmar um comprometimento do servidor.

2. Evidências encontradas

* 4 autenticações malsucedidas envolvendo os usuários `admin`, `root` e `analyst`.
* 2 autenticações bem-sucedidas envolvendo os usuários `analyst` e `backup`.
* IP `192.0.2.45` associado às falhas e ao login de `analyst`.
* IP `192.0.2.80` associado ao login de backup.
* O usuário analyst executou `/usr/bin/id` com sudo.
* A conta `backup` utilizou chave pública para se autenticar e acessar o servidor.

## 3. Linha do tempo

| Horário | Evento |
| - | - |
| 08:10:12 | Primeira tentativa malsucedida para admin |
| 08:10:18 | Segunda tentativa malsucedida para admin |
| 08:10:24 | Tentativa malsucedida para root |
| 08:11:02 | Tentativa malsucedida para analyst |
| 08:11:15 | Autenticação bem-sucedida de analyst |
| 08:12:30 | Abertura da sessão SSH de analyst |
| 08:14:05 | Execução de /usr/bin/id com sudo |
| 08:16:42 | Encerramento da sessão de analyst |
| 08:20:01 | Autenticação por chave pública de backup |
| 08:20:10 | Abertura da sessão SSH de backup |

## 4. Atividades suspeitas identificadas

### 4.1 Tentativas consecutivas de autenticação

A ocorrência de quatro tentativas malsucedidas em um intervalo de aproximadamente 50 segundos pode indicar uma tentativa de força bruta ou descoberta de credenciais.

### 4.2 Acesso bem-sucedido após falhas

O acesso bem-sucedido à conta `analyst`, originado do mesmo endereço IP responsável pelas tentativas anteriores, merece atenção e precisa ser validado.

### 4.3 Acesso à conta `backup`

A autenticação posterior utilizando chave pública SSH merece investigação adicional para verificar se a chave utilizada pertence a um usuário autorizado.

É importante destacar que não há evidências suficientes para afirmar que essa chave foi inserida por um invasor.

## 5. Conclusão

A análise identificou uma sequência de eventos que merece atenção, principalmente pelas tentativas consecutivas de autenticação malsucedidas seguidas de um acesso bem-sucedido à conta analyst.

Também foi identificado um acesso posterior à conta backup, utilizando autenticação por chave pública e outro endereço IP.

Embora esses acontecimentos possam indicar uma atividade maliciosa, também existe a possibilidade de serem acessos legítimos.

Portanto, não é possível confirmar que houve invasão ou escalonamento de privilégios apenas com os registros disponíveis.

## 6. Limitações da investigação

Esta investigação foi realizada exclusivamente com base no arquivo auth.log disponibilizado no laboratório.

As principais limitações identificadas foram:

* Ausência de informações que permitam confirmar a legitimidade dos endereços IP.
* Ausência do histórico completo de comandos executados durante as sessões.
* Ausência de informações sobre a origem e o proprietário da chave pública utilizada por backup.
* Ausência de outros registros do sistema para correlacionar os acontecimentos.
* Impossibilidade de confirmar se os acessos foram realizados por usuários legítimos ou por terceiros não autorizados.

> **Resultado final:** foram identificados indicadores de atividade suspeita, mas não existem evidências suficientes para confirmar um comprometimento do servidor.