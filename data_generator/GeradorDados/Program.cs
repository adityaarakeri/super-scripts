using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

namespace GeradorDados
{
    class Program
    {
        static List<Procedimento> proc = new List<Procedimento>();
        static string WORD_LIST_PATH = @"F:\Projetos\C#\GeradorDados\GeradorDados\bin\Debug\";
        static void Main(string[] args)
        {
            Console.WriteLine("Clientes a serem gerados: ");
            string r = Console.ReadLine().ToString();

            Console.WriteLine("Procedimentos a serem gerados: ");
            string p = Console.ReadLine().ToString();

            Console.WriteLine("Atendimentos a serem gerados: ");
            string at = Console.ReadLine().ToString();

            int total = int.Parse(r);
            for (int i = 0; i < total; i++)
            {
                gerarQuerys();
            }

            
            int tp = int.Parse(p);
            for (int i = 0; i < tp; i++)
            {
                gerarProcedimentos(i);
            }
            
            int atp = int.Parse(at);
            for (int i = 0; i < atp; i++)
            {
                gerarAtendimento(i, total);
            }

            Console.WriteLine(total.ToString() + " clientes gerados!");
            Console.WriteLine(tp.ToString() + " procedimentos gerados!");
            Console.WriteLine(atp.ToString() + " atendimentos gerados!");
            Console.ReadKey();
        }

        static void gerarQuerys()
        {
            int firstNameCount = File.ReadLines(WORD_LIST_PATH + "first-names.txt").Count();
            int lastNameCount = File.ReadLines(WORD_LIST_PATH + "middle-names.txt").Count();
            int wordsCount = File.ReadLines(WORD_LIST_PATH + "palavras.txt").Count();
            int citiesCount = File.ReadLines(WORD_LIST_PATH + "cidades.txt").Count();
            int ufCount = File.ReadLines(WORD_LIST_PATH + "uf.txt").Count();

            Random random = new Random(Guid.NewGuid().GetHashCode());
            int lineNumber = random.Next(2, firstNameCount);

            string firstName = File.ReadLines(WORD_LIST_PATH + "first-names.txt").Skip(lineNumber - 2).Take(1).First();

            lineNumber = random.Next(2, lastNameCount);
            string lastName = File.ReadLines(WORD_LIST_PATH + "first-names.txt").Skip(lineNumber - 2).Take(1).First();

            lineNumber = random.Next(2, citiesCount);
            string cidade = File.ReadLines(WORD_LIST_PATH + "cidades.txt").Skip(lineNumber - 2).Take(1).First();

            lineNumber = random.Next(2, ufCount);
            string uf = File.ReadLines(WORD_LIST_PATH + "uf.txt").Skip(lineNumber - 2).Take(1).First();

            string celular = random.Next(11, 99).ToString() + "9";
            celular += random.Next(0, 9).ToString() + random.Next(81000000, 99999999).ToString();

            string telefone = random.Next(11, 99).ToString();
            telefone += random.Next(20000000, 39999999).ToString();

            string endereco = File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + " " +
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First();

            string bairro = File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + " " + 
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First();

            string complemento = File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + " " + 
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + 
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + " " + 
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + 
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + " " + 
                File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First();

            if (random.Next(Int32.MinValue, Int32.MaxValue) % 2 == 0)
                complemento = "";

            string numero = random.Next(0, 9999).ToString();
            string cep = random.Next(0, 9999999).ToString().PadLeft(8, '0');
            string cpf = random.Next(100000000, 999999999).ToString().PadLeft(9, '0');

            int soma = 0;
            int peso = 10;
            int resto = 0;

            for (int i = 0; i < (cpf.ToCharArray().Length); i++)
            {
                soma += int.Parse(cpf.ToCharArray()[i].ToString()) * peso;
                peso--;
            }
            resto = soma % 11;

            int dv1 = 11 - resto;
            if (dv1 > 9)
                dv1 = 0;

            soma = 0;
            peso = 11;
            for (int i = 0; i < (cpf.ToCharArray().Length); i++)
            {
                soma += int.Parse(cpf.ToCharArray()[i].ToString()) * peso;
                peso--;
            }
            soma += dv1 * peso;

            resto = soma % 11;

            int dv2 = 11 - resto;
            if (dv2 > 9)
                dv2 = 0;

            cpf += dv1.ToString() + dv2.ToString();

            string dia = random.Next(1, 31).ToString();
            string mes = random.Next(1, 12).ToString();
            string ano = random.Next(1950, 2020).ToString();

            dia = dia.PadLeft(2, '0');
            mes = mes.PadLeft(2, '0');

            string nascimento = ano + "-" + mes + "-" + dia;
            string email = File.ReadLines(
                WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1).First() + 
                "@" + File.ReadLines(WORD_LIST_PATH + "palavras.txt")
                .Skip(random.Next(2, wordsCount) - 2)
                .Take(1)
                .First() + ".com";

            StringBuilder sbReturn = new StringBuilder();
            var arrayText = email.Normalize(NormalizationForm.FormD).ToCharArray();
            foreach (char letter in arrayText)
            {
                if (CharUnicodeInfo.GetUnicodeCategory(letter) != UnicodeCategory.NonSpacingMark)
                    sbReturn.Append(letter);
            }
            
            Pessoa p = new Pessoa();
            p.nome = firstName;
            p.sobrenome = lastName;
            p.cpfcnpj = cpf;
            p.nascimento = nascimento;
            p.cep = cep;
            p.endereco = endereco;
            p.numero = numero;
            p.complemento = complemento;
            p.bairro = bairro;
            p.cidade = cidade;
            p.uf = uf;
            p.telefone = telefone;
            p.celular = celular;
            p.email = email;

            string output = JsonConvert.SerializeObject(p);

            File.AppendAllText("query.txt",
                   output + Environment.NewLine);
        }


        static void gerarProcedimentos(int index)
        {
            int procedimentosCount = File.ReadLines(WORD_LIST_PATH + "procedimentos.txt").Count();

            Random random = new Random(Guid.NewGuid().GetHashCode());
            int lineNumber = random.Next(2, procedimentosCount);

            string procedimento = File.ReadLines(WORD_LIST_PATH + "procedimentos.txt").Skip(lineNumber - 2).Take(1).First();

            double valor = random.NextDouble() * (20000 - 100) + 100;
            int time = random.Next(10, 721);                        

            Procedimento p = new Procedimento();
            p.id = index;
            p.nome = procedimento;
            p.valor = valor;

            string output = JsonConvert.SerializeObject(p);
            File.AppendAllText("query.txt",
                  output + Environment.NewLine);

            proc.Add(p);
        }

        static void gerarAtendimento(int index, int client)
        {
            Random random = new Random(Guid.NewGuid().GetHashCode());
            DateTime start = new DateTime(2020, 05, 19);
            start.AddDays(random.Next(1, 61));

            int hora = random.Next(0, 24);
            int minuto = random.Next(0, 60);

            string data = start.Year + "-" + start.Month.ToString("00") + "-" + start.Day.ToString("00");
            string horaAte = hora.ToString("00") + ":" + minuto.ToString("00") + ":00";

            List<Procedimento> procs = new List<Procedimento>();
            random = new Random(Guid.NewGuid().GetHashCode());
            int maxProx = random.Next(1, proc.Count/2) ;

            for(int i = 0; i < maxProx; i++)            
                procs.Add(proc[random.Next(1, maxProx)]);

            double total = 0;

            for (int i = 0; i < procs.Count; i++)
            {
                total += procs[i].valor;
            }

           double desconto = random.NextDouble() * total;

            double subtotal = total - desconto;

            int recebido = random.Next(0, 2);

            Pagamento p = new Pagamento();
            p.total = String.Format("{0:0.00}", total).Replace(",", ".");
            p.desconto = String.Format("{0:0.00}", desconto).Replace(",", ".");
            p.subtotal = String.Format("{0:0.00}", subtotal).Replace(",", ".");
            p.data = data;
            p.recebido = recebido;
            string output = JsonConvert.SerializeObject(p);
            File.AppendAllText("query.txt",
                  output + Environment.NewLine);

            int clientRandom = random.Next(1, client + 1);

            Atendimento a = new Atendimento();
            a.obs = "";
            a.data_atendimento = data;
            a.hora_atendimento = horaAte;
            a.recebimentos_idrecebimentos = (index + 1).ToString();
            a.clientes_idclientes = clientRandom.ToString();
            a.procs = proc;
            output = JsonConvert.SerializeObject(a);
            File.AppendAllText("query.txt",
                  output + Environment.NewLine);
        }
    }

    class Pagamento
    {
        public string total { get; set; }
        public string desconto { get; set; }
        public string subtotal { get; set; }
        public string data { get; set; }
        public int recebido { get; set; }
    }

    class Procedimento
    {
        public int id { get; set; }
        public String nome { get; set; }
        public double valor { get; set; }
    }

    class Atendimento
    {
        public string obs { get; set; }
        public string data_atendimento { get; set; }
        public string hora_atendimento { get; set; }
        public string recebimentos_idrecebimentos { get; set; }
        public string clientes_idclientes { get; set; }
        public List<Procedimento> procs { get; set; }
    }

    class Pessoa
    {
        public string nome { get; set; }
        public string sobrenome { get; set; }
        public string cpfcnpj { get; set; }
        public string nascimento { get; set; }
        public string cep { get; set; }
        public string endereco { get; set; }
        public string numero { get; set; }
        public string complemento { get; set; }
        public string bairro { get; set; }
        public string cidade { get; set; }
        public string uf { get; set; }
        public string telefone { get; set; }
        public string celular { get; set; }
        public string email { get; set; }
    }
}
