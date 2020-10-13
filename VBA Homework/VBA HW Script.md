Sub WallStreetHW():

'Loop worksheets'

For Each WS In Worksheets

WS.Activate

'Insert Column Headers'
    
WS.Cells(1, 9).Value = "Ticker"
WS.Cells(1, 10).Value = "Yearly Change"
WS.Cells(1, 11).Value = "Percentage Change"
WS.Cells(1, 12).Value = "Total Stock Volume"

 'Declarations and Assignments for Initial Variables'
 
Dim TickerSymbol As String
Dim OpenPrice As Double
Dim ClosePrice As Double
Dim TotalStockVolume As Double
Dim YearlyChange As Double
Dim PercentageChange As Double
Dim TickerCounter As Integer
Dim MaxRows As Long
Dim GreatestPercentageIncrease As Double
Dim GreatestPercentageIncreaseticker As String
Dim GreatestPercentageDecrease As Double
Dim GreatestPercentageDecreaseTicker As String
Dim greatest_stock_volume As Double
Dim greatest_stock_volume_ticker As String

'Initial values'

TickerCounter = 0
TickerSymbol = ""
YearlyChange = 0
OpenPrice = 0
PercentageChange = 0
TotalStockVolume = 0
MaxRows = WS.Cells(Rows.Count, "A").End(xlUp).Row

    
    For i = 2 To MaxRows
    TickerSymbol = Cells(i, 1).Value
        
  'Open Price'
  
        If OpenPrice = 0 Then
            OpenPrice = Cells(i, 3).Value
        End If
        
        TotalStockVolume = TotalStockVolume + Cells(i, 7).Value
        
    'Determine Ticker Value, comparing cell value below to above to find different TickerSymbol'
    
        If Cells(i, 1).Value <> Cells(i + 1, 1) Then
            TickerCounter = TickerCounter + 1
            Cells(TickerCounter + 1, 9) = TickerSymbol
            
      'Close Price and Yearly Change'
      
      
        ClosePrice = Cells(i, 6)
        YearlyChange = ClosePrice - OpenPrice
        Cells(TickerCounter + 1, 10).Value = YearlyChange
            
            
            'Conditional Colour Formatting Per Negative or Positive Yearly Change'
            If YearlyChange > 0 Then
                Cells(TickerCounter + 1, 10).Interior.ColorIndex = 4
            ElseIf YearlyChange < 0 Then
                Cells(TickerCounter + 1, 10).Interior.ColorIndex = 3
            End If
            
             'Convert Percentage Change into %
             
             Cells(TickerCounter + 1, 11).Value = Format(PercentageChange, "Percent")
            
            ' Calculate percentage change value for ticker.
            
            If OpenPrice = 0 Then
                PercentageChange = 0
            Else
                PercentageChange = (YearlyChange / OpenPrice)
            End If
            
            
            ' Reset Open Price'
            OpenPrice = 0
            
            ' Add total stock volume value to the appropriate cell in each worksheet.
            Cells(TickerCounter + 1, 12).Value = TotalStockVolume
            
            'Reset Stock Volume
            TotalStockVolume = 0
        End If
        
    Next i
    
    'Challenge Section'
    
    'Challenge Section: Inserting Column Titles/Headers'
    
    WS.Range("O2").Value = "Greatest % Increase"
    WS.Range("O3").Value = "Greatest % Decrease"
    WS.Range("O4").Value = "Greatest Total Volume"
    WS.Range("P1").Value = "Ticker"
    WS.Range("Q1").Value = "Value"
    
    'Starting Values'
    
    GreatestPercentageIncrease = Cells(2, 11).Value
    GreatestPercentageIncreaseticker = Cells(2, 9).Value
    GreatestPercentageDecrease = Cells(2, 11).Value
    GreatestPercentageDecreaseTicker = Cells(2, 9).Value
    greatest_stock_volume = Cells(2, 12).Value
    greatest_stock_volume_ticker = Cells(2, 9).Value
    
    MaxRows = WS.Cells(Rows.Count, "I").End(xlUp).Row
    For i = 2 To MaxRows
    
        'Challenges: Greatest Total Volume Section'
    
        If Cells(i, 12).Value > greatest_stock_volume Then
            greatest_stock_volume = Cells(i, 12).Value
            greatest_stock_volume_ticker = Cells(i, 9).Value
        End If
    
        'Challenge Section:Greatest % Increase & Greatest % Decrease'

        If Cells(i, 11).Value > GreatestPercentageIncrease Then
            GreatestPercentageIncrease = Cells(i, 11).Value
            GreatestPercentageIncreaseticker = Cells(i, 9).Value
        End If
        
        If Cells(i, 11).Value < GreatestPercentageDecrease Then
            GreatestPercentageDecrease = Cells(i, 11).Value
            GreatestPercentageDecreaseTicker = Cells(i, 9).Value
        End If
        
        
    Next i
    
    'Final Input for Value for Challenges Section
    
    Cells(2, 16).Value = Format(GreatestPercentageIncreaseticker, "Percent")
    Cells(2, 17).Value = Format(GreatestPercentageIncrease, "Percent")
    Cells(3, 16).Value = Format(GreatestPercentageDecreaseTicker, "Percent")
    Cells(3, 17).Value = Format(GreatestPercentageDecrease, "Percent")
    Cells(4, 16).Value = greatest_stock_volume_ticker
    Cells(4, 17).Value = greatest_stock_volume
    
Next WS


End Sub
