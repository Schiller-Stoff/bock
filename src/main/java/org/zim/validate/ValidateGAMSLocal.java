package org.zim.validate;

import picocli.CommandLine.Command;

@Command(name = "validate", description = "Validates gams local setup on your dec machine")
public class ValidateGAMSLocal implements Runnable {
  
  public void run(){
    System.out.println("Validating now gams local setup...");
  }
}
