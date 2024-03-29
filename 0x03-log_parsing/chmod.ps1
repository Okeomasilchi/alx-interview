param (
    [Parameter(Mandatory=$true)]
    [string]$FileName
)

try {
    # Check if the file exists
    if (Test-Path $FileName) {
        # Prompt user for new file mode
        $NewMode = Read-Host "Enter the new file mode (e.g., '755', '644'):"
        
        # Convert numeric file mode to FileSystemRights enumeration value
        $FileSystemRights = @{
            '777' = 'FullControl'
            '755' = 'Modify, ReadAndExecute, Read'
            '644' = 'ReadAndExecute, Read'
        }

        if ($FileSystemRights.ContainsKey($NewMode)) {
            $Rights = $FileSystemRights[$NewMode]
            
            # Get the current ACL of the file
            $acl = Get-Acl $FileName
            
            # Define the new rule
            $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone",$Rights,"Allow")
            
            # Add the new rule to the ACL
            $acl.SetAccessRule($rule)
            
            # Set the modified ACL back to the file
            Set-Acl -Path $FileName -AclObject $acl
            
            Write-Host "File mode changed successfully."
        } else {
            Write-Host "Invalid file mode: $NewMode"
        }
    } else {
        Write-Host "File not found: $FileName"
    }
} catch {
    Write-Host "An error occurred: $_"
}
