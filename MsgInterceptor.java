import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.xml.soap.SOAPException;

import org.apache.cxf.frontend.MethodDispatcher;
import org.apache.cxf.interceptor.Fault;
import org.apache.cxf.message.Exchange;
import org.apache.cxf.message.Message;
import org.apache.cxf.phase.AbstractPhaseInterceptor;
import org.apache.cxf.phase.Phase;
import org.apache.cxf.service.Service;
import org.apache.cxf.service.model.BindingOperationInfo;
import org.apache.cxf.transport.http.AbstractHTTPDestination;

import com.ceair.talent.ehcache.impl.CouponPurviewCache;
import com.ebiz.framework.exception.BaseAppException;
import com.ebiz.framework.service.BaseService;

public class MsgInterceptor extends AbstractPhaseInterceptor<Message>{
	private CouponPurviewCache cpCache = (CouponPurviewCache)BaseService.getBeanStatic("CouponPurviewCache");
	public MsgInterceptor(String phase) {
		super(phase);
	}
	public MsgInterceptor() {
		super(Phase.RECEIVE);  //指定加载拦截器时间
	}
	
	//拦截器消息处理
	public void handleMessage(Message message) {
		System.out.println(message.get(message.HTTP_REQUEST_METHOD)); //获取消息传递方式 GET 或者 POST
		 InputStream is = message.getContent(InputStream.class); //这个方法发是获取post方法的输入数据
		 try {
			ByteArrayOutputStream outStream = new ByteArrayOutputStream();
			byte[] data = new byte[4096];
			int count = -1;
			while ((count = is.read(data, 0, 4096)) != -1)
				outStream.write(data, 0, count);

			data = null;
			System.out.println(new String(outStream.toByteArray(), "UTF-8")); //转码
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
         System.out.println(is.toString());
	}
	//获取当前requestIP
	private  String getRemoteIP(HttpServletRequest request) {

		String ip = request.getHeader("x-forwarded-for");
        if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) {
            ip = request.getHeader("Proxy-Client-IP");
        }
        if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) {
            ip = request.getHeader("WL-Proxy-Client-IP");
        }
        if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) {
            ip = request.getRemoteAddr();
        }
        return ip;
    }
	
	private boolean checkIsAllowed(String Ip, String requestMethod){
		try {
			List<String> allowedIps = cpCache.getPurviewFromcache(requestMethod);
			for(String str : allowedIps){
				if(str.equals(Ip)){
					return true; // 只要有一个命中 返回真
				}
			}
		} catch (BaseAppException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return false;
	}
}
