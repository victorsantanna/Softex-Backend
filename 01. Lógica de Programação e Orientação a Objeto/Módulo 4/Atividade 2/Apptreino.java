//Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva três ou mais objetos para testar o código.

public class Apptreino {


    public static void main(String[] args){

        Treino treinoA = new Treino();
        treinoA.nome = " Dorsal";
        treinoA.tipo = "musculação";
        treinoA.duracao = 90;
        treinoA.intensidade = "moderada";

       
        System.out.format("Seu Treino é do tipo %s com grupo muscular %s, com duração de %d minutos e intensidade %s .", treinoA.tipo, treinoA.nome, treinoA.duracao, treinoA.intensidade);
        
    }
}