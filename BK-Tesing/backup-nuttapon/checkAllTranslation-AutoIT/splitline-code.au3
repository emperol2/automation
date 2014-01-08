Local $file = FileOpen(@ScriptDir & "\log.txt", 0)
Local $result = FileOpen(@ScriptDir & "\result.txt", 2)


; Check if file opened for reading OK
If $file = -1 Then
    MsgBox(0, "Error", "Unable to open file.")
    Exit
EndIf

MsgBox(0,"","Application Start")

; Read in lines of text until the EOF is reached
While 1
    Local $line = FileReadLine($file)
    If @error = -1 Then ExitLoop
	$hasnot = StringInStr($line, "result: has not")
	if $hasnot > 0 Then
		;MsgBox(0, "Line read:", $line)
		
			$result = FileOpen(@ScriptDir & "\result.txt", 1)
	
			If $result = -1 Then
				MsgBox(0, "Error", "Unable to open file.")
				Exit
			EndIf	
			
			FileWrite($result, $line & @CRLF)	
			
	EndIf
	
	FileClose($result)
WEnd

MsgBox(0,"","Application Stop")

FileClose($file)

