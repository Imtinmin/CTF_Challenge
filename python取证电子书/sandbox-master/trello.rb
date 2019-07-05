class Trello

  LETTERS = "acdegilmnoprstuw"

  def self.trello_hash(string)
    h = 7
    string.each_char do |letter|
      h = h * 37 + LETTERS.index(letter)
    end

    return h
  end

  def self.trello_letters(hash)
    h = hash
    pepper = []
    output = []

    until h == 7 do
      pepper.push(h)

      h = h / 37
    end
    pepper.push(7)
    pepper.reverse!

    (1..(pepper.length - 1)).each do |index|
      letter_index = pepper[index] - (pepper[index - 1] * 37)
      output.push(LETTERS.chars[letter_index])
    end

    return output.join
  end
end
