package com.de;

import java.util.regex.Matcher;
import java.util.regex.Pattern;


/****
 * 学好正则表达式 走遍天下都不怕。
 * @author cocal
 *
 */
public class JavaRegular {
	
	private static void test1(){
		String rex = "[ABC]";
		Pattern p = Pattern.compile(rex);
		Matcher m = p.matcher("Acde");
		if(m.find()){
			System.out.println("Done!");
		}else{
			System.out.println("HEHE");
		}
	}
	
	public static void main(String[] argv){
		//run
		JavaRegular.test1();
	}
}
