package com.de;

import java.lang.reflect.Field;

class Demo2{
	private int i;
	private String j;
	private String k = "3";
	Demo2(int i,String j){
		this.i = i;
		this.j = j;
	}
}
public class testJava {
	public static void main(String[] args){
		System.out.println("--");
		Demo2 d = new Demo2(1,"sb");
		try {
			Class obj = Class.forName(d.getClass().getName());
			Field[] field = obj.getDeclaredFields();
			System.out.println(field.length);
			for(Field f : field ){
				f.setAccessible(true);
				System.out.println(f.getType().toString()); //获得类型
				Object val =  f.get(d);
				System.out.println(val);
			}
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IllegalArgumentException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
