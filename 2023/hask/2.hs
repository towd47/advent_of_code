{-# LANGUAGE NoImplicitPrelude #-}
import Data.Maybe
import System.IO
import Data.Function
import Data.List
import Data.Bool
import Data.Text hiding ( map, lines, null, isSuffixOf, head)
import Data.Text.Read
import Prelude

main = do
    s <- readFile "../inputs/2"
    print $ solve part1 s
    print $ solve part2 s


solve :: (String -> Maybe Int) -> String -> Int
solve f = sum . map (line f) . lines

line :: (String -> Maybe Int) -> String -> Int
line f s | isNothing res = 0
         | otherwise = fromJust res
         where
            res = f s

part1 :: String -> Maybe Int
part1 s | areValid (map unpack (listPulls pulls)) = Just (read (unpack (getGameNum gameId)))
        | otherwise = Nothing
        where
            (gameId:pulls) = getVals (pack s)

part2 :: String -> Maybe Int
part2 s = Just $ product (getMaxForEachColor (map unpack (listPulls pulls)) 0 0 0)
        where
            (_:pulls) = getVals (pack s)

getMaxForEachColor :: [String] -> Int -> Int -> Int -> [Int]
getMaxForEachColor (x:xs) r g b | "red" `isSuffixOf` x = getMaxForEachColor xs (max r (getDraws (pack x))) g b
                                | "green" `isSuffixOf` x = getMaxForEachColor xs r (max g (getDraws (pack x))) b
                                | "blue" `isSuffixOf` x = getMaxForEachColor xs r g (max b (getDraws (pack x)))
getMaxForEachColor _ r g b = [r, g, b]

getDraws pull = read (unpack num)
            where
                (num:_) = splitOn (pack " ") pull

getGameNum :: Text -> Text
getGameNum s = splitOn (pack " ") s !! 1

getVals :: Text -> [Text]
getVals = splitOn (pack ": ")

areValid :: [String] -> Bool
areValid = Data.List.all isValidAmount


listPulls :: [Text] -> [Text]
listPulls [s] = Data.List.concat (map (splitOn (pack ", ")) (splitOn (pack "; ") s))

isValidAmount :: String -> Bool
isValidAmount s = read (unpack x) <= getMax (unpack y)
        where
            (x:y:xs) = splitOn (pack " ") (pack s)

getMax :: Num a => String -> a
getMax s | s == "green" = 13
         | s == "blue" = 14
         | s == "red" = 12