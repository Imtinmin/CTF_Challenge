require "dhash-vips"

hash1 = DHashVips::IDHash.fingerprint "dog1.jpg"
hash2 = DHashVips::IDHash.fingerprint "dog2.jpg"

distance = DHashVips::IDHash.distance hash1, hash2
if distance < 15
  puts "Images are very similar"
elsif distance < 25
  puts "Images are slightly similar"
else
  puts "Images are different"
end
