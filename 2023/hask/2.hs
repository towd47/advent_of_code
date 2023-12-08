{-# LANGUAGE NoImplicitPrelude #-}
import Data.Maybe
import System.IO
import Data.Function
import Data.List
import Data.Bool
import Data.Text hiding ( map, lines)
import Data.Text.Read
import Prelude

main = do
    s <- readFile "../inputs/2"
    print $ solve part1 s


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

getGameNum s = splitOn (pack " ") s !! 1

getVals = splitOn (pack ": ")

areValid = Data.List.all isValidAmount


listPulls :: [Text] -> [Text]
listPulls [s] = Data.List.concat (map (splitOn (pack ", ")) (splitOn (pack "; ") s))
-- [[1 green, 2 red, 3 blue], [1 blue, 4 red]]

isValidAmount :: String -> Bool
isValidAmount s = read (unpack x) <= getMax (unpack y)
        where
            (x:y:xs) = splitOn (pack " ") (pack s)

getMax :: Num a => String -> a
getMax s | s == "green" = 13
         | s == "blue" = 14
         | s == "red" = 12