// OCR a scanned PDF with the macOS Vision framework (no installs). Usage: swift vision_ocr.swift IN.pdf OUT.txt
import Foundation
import PDFKit
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count == 3, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else { print("usage: IN.pdf OUT.txt"); exit(1) }
var out = ""
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let box = page.bounds(for: .mediaBox)
    let scale: CGFloat = 3.0
    let w = Int(box.width * scale), h = Int(box.height * scale)
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0,
                              space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue) else { continue }
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1)); ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: scale, y: scale); page.draw(with: .mediaBox, to: ctx)
    guard let img = ctx.makeImage() else { continue }
    let req = VNRecognizeTextRequest(); req.recognitionLevel = .accurate; req.usesLanguageCorrection = false
    try? VNImageRequestHandler(cgImage: img, options: [:]).perform([req])
    let lines = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }
    out += "\n[page \(i + 1)]\n" + lines.joined(separator: "\n") + "\n"
}
try out.write(toFile: args[2], atomically: true, encoding: .utf8)
print("pages \(doc.pageCount) chars \(out.count)")
