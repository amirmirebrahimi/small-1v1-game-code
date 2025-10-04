import champion


class warrior(champion):
  
  def Special_ability(self,enemy):
        distance = abs(self.Location - enemy.Location)
        if distance < 20:
            enemy.Health -= self.Damage * 2
            self.Health += 0.3 * self.Damage
            
    



