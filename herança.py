class Empregado:
    """Classe base com atributos comuns."""
    def __init__(self, nome: str, salario_base: float):
        if salario_base < 0:
            raise ValueError("salario_base deve ser >= 0")
        self.nome = nome
        self.salario_base = float(salario_base)

    def calcular_salario(self) -> float:
        """Retorna o salário total (padrão = salario_base)."""
        return self.salario_base

    def __str__(self) -> str:
        return f"{self.nome} - Salário base: R$ {self.salario_base:.2f}"


class Gerente(Empregado):
    """Gerente: tem um bônus fixo além do salário base."""
    def __init__(self, nome: str, salario_base: float, bonus_fixo: float):
        super().__init__(nome, salario_base)
        if bonus_fixo < 0:
            raise ValueError("bonus_fixo deve ser >= 0")
        self.bonus_fixo = float(bonus_fixo)

    def calcular_salario(self) -> float:
        """Salário total = salário base + bônus fixo."""
        return self.salario_base + self.bonus_fixo

    def detalhes(self) -> str:
        return (f"{self.nome} (Gerente) - Base: R$ {self.salario_base:.2f}, "
                f"Bônus: R$ {self.bonus_fixo:.2f}, "
                f"Total: R$ {self.calcular_salario():.2f}")


class Vendedor(Empregado):
    """Vendedor: ganha comissão sobre as vendas além do salário base."""
    def __init__(self, nome: str, salario_base: float, total_vendas: float, taxa_comissao: float):
        super().__init__(nome, salario_base)
        if total_vendas < 0:
            raise ValueError("total_vendas deve ser >= 0")
        if taxa_comissao < 0:
            raise ValueError("taxa_comissao deve ser >= 0")
        self.total_vendas = float(total_vendas)
        self.taxa_comissao = float(taxa_comissao)  # ex: 0.05 = 5%

    def calcular_comissao(self) -> float:
        return self.total_vendas * self.taxa_comissao

    def calcular_salario(self) -> float:
        """Salário total = salário base + comissão sobre vendas."""
        return self.salario_base + self.calcular_comissao()

    def detalhes(self) -> str:
        return (f"{self.nome} (Vendedor) - Base: R$ {self.salario_base:.2f}, "
                f"Vendas: R$ {self.total_vendas:.2f}, "
                f"Taxa: {self.taxa_comissao * 100:.1f}%, "
                f"Comissão: R$ {self.calcular_comissao():.2f}, "
                f"Total: R$ {self.calcular_salario():.2f}")


if __name__ == "__main__":
    # Exemplos de teste
    gerente = Gerente(nome="Ana Silva", salario_base=7000.00, bonus_fixo=1500.00)
    vendedor = Vendedor(nome="Carlos Souza", salario_base=2500.00, total_vendas=30000.00, taxa_comissao=0.05)

    # Mostrando detalhes
    print(gerente.detalhes())
    print(vendedor.detalhes())

    # Demonstração de polimorfismo:
    funcionarios = [gerente, vendedor]
    print("\nResumo dos salários (polimorfismo):")
    for f in funcionarios:
        # chama calcular_salario() da classe concreta
        print(f"- {f.nome}: R$ {f.calcular_salario():.2f}")