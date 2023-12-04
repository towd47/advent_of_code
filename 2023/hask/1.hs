import Data.Char
import Data.List (isPrefixOf)
import Data.Maybe (fromMaybe, fromJust, catMaybes, mapMaybe)

main = do
    s <- readFile "../inputs/1"
    print $ totS (lines s) 0
    print $ p2 $ lines s

nFromS :: String -> String -> Int
nFromS a acc | null a = read (head acc : [last acc]) :: Int
                | isDigit (head a) = nFromS (tail a) (acc ++ take 1 a)
                | otherwise = nFromS (tail a) acc

totS :: [String] -> Int -> Int
totS a acc | null a = acc
            | otherwise = totS (tail a) (acc + nFromS (head a) [])

p2 lines = sum $ map calibrationVal lines

calibrationVal x = let val = catMaybes (getAllNums x)
                    in 10 * head val + last val 

getAllNums :: [Char] -> [Maybe Int]
getAllNums s | null s = []
            | otherwise = getNums s (zipWithNums (match True)) : getAllNums (tail s)

getNums :: String -> [(String, Int)] -> Maybe Int
getNums s (x:xs) | fst x `isPrefixOf` s = Just $ snd x
            | null xs = Nothing
            | otherwise = getNums s xs

consMaybe :: a -> Maybe [a] -> Maybe [a]
consMaybe _ Nothing = Nothing
consMaybe x (Just xs) = Just (x:xs)

match :: Bool -> [String]
match s | not s = map show [1 .. 10]
        | otherwise = (++) (map show [1 .. 9]) ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

zipWithNums :: (Num b, Enum b) => [a] -> [(a, b)]
zipWithNums a = zip a $ (++) [1..9] [1..9]