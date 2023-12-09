{-# LANGUAGE OverloadedStrings #-}

import Data.Char
import Data.Bool

main = do
    a <- readFile "../inputs/6"
    print $ parse a
parse = map (read @Int) . words . map (bool ' ' <*> isDigit)