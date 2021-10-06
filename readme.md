
# gamsFrontCLI

Very basic cli-tool to help setting up a gams-project on gams4+ from perspective of frontend-development.

## Aims

1. Simplify
  - setting up the dev assets shpuld be
2. Centralize
  - avoid copying of old code. Make sure to spread best practices / bug fixes etc.
3. Abstract away:
  - knowledge about different repositories and other implementation details.
4. Validate:
  - integrate frontend test possiblity into the tool


## Example cli calls

```sh

# calling validate subcommand
c:; cd 'c:\Users\stoffse\Documents\Programmieren\java\gamsfront-cli'; & 'c:\Users\stoffse\.vscode\extensions\vscjava.vscode-java-debug-0.36.0\scripts\launcher.bat' 'C:\Program Files\Eclipse Foundation\jdk-11.0.12.7-hotspot\bin\java.exe' '-Dfile.encoding=UTF-8' '@C:\Users\stoffse\AppData\Local\Temp\cp_2e9hvov2ofwsiazlht21bzn8v.argfile' 
'org.zim.GamsFrontCLICommand' validate

# calling just the main script
c:; cd 'c:\Users\stoffse\Documents\Programmieren\java\gamsfront-cli'; & 'c:\Users\stoffse\.vscode\extensions\vscjava.vscode-java-debug-0.36.0\scripts\launcher.bat' 'C:\Program Files\Eclipse Foundation\jdk-11.0.12.7-hotspot\bin\java.exe' '-Dfile.encoding=UTF-8' '@C:\Users\stoffse\AppData\Local\Temp\cp_2e9hvov2ofwsiazlht21bzn8v.argfile' 
'org.zim.GamsFrontCLICommand' -v


```