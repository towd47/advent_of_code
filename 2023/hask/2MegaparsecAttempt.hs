{-# LANGUAGE OverloadedStrings #-}

import Text.Megaparsec hiding (parse)
import Text.Megaparsec.Char
import Text.Megaparsec.Char.Lexer ( decimal )
import Data.Text hiding (head, lines)
import Data.Void
import Control.Applicative hiding (many, some)
import Data.Map.Strict as M
import Data.Functor
import Data.Maybe

type Parser = Parsec Void Text
main = do
    s <- readFile "../inputs/2"
    cards <- Prelude.map parse (lines s) 
    print $ p1 cards

gameParser :: Parser (Int, [Map Text Int])
gameParser =
    (,) <$> gameNum <*> reveals
    where
        gameNum = string "Game " *> decimal <* string ": "
        reveals = sepBy1 pulls (string "; ")
        pulls = sepBy1 pull (string ", ") <&> M.fromList
        pull = do
            pullNum <- decimal
            spaceChar
            color <- some letterChar <&> pack
            pure (color, pullNum)

parse = fromJust . parseMaybe gameParser


p1 = sum . Prelude.map validPull

validPull s = s 